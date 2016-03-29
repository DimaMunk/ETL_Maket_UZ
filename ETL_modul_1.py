import openpyxl
import GetValueOfArea
import psycopg2
import warnings


def ExportInDB(unitName, pokazatelKetegory, IDpokazatel_name, rows_count, columns_count,
               rows_end, columns_end, ColumnTerrName, RowDate, mode, ExcelName = 'default', dbname = "data",
               dbhost = '192.168.47.26', dbpassword = '12345678', dbuser = 'postgres'):

    warnings.simplefilter("ignore")
    error = False

    if ExcelName == 'default': ExcelName = IDpokazatel_name
    defaultColumnCount = columns_count
#DB connecting
    try:
        connection = psycopg2.connect('''dbname = {} user = {}
                                        host = {}  password = {} '''.format(dbname, dbuser, dbhost, dbpassword))
    except Exception as err:
        error = True
        print('Can\'t connect to DB',err)
    cur = connection.cursor()



###############Get id pokazatel

    cur.execute(''' SELECT dim_pokazatel.id FROM "{}".public.dim_pokazatel
                    WHERE name = %s;'''.format(dbname),(IDpokazatel_name,))
    DBresponse = cur.fetchall()
    if len(DBresponse) == 0:
        cur.execute(''' SELECT max(id) FROM "{}".public.dim_pokazatel'''.format(dbname))
        DBresponse = cur.fetchall()

        if DBresponse[0][0] == None:
            IDpokazatel = 1
        else:
            IDpokazatel = DBresponse[0][0] + 1

        cur.execute(''' INSERT INTO public.dim_pokazatel(id, name, name_full, category)
        VALUES (%s,%s,%s,%s); ''',(IDpokazatel, IDpokazatel_name, IDpokazatel_name, pokazatelKetegory,))
        connection.commit()

    else:
        IDpokazatel = DBresponse[0][0]

########################get id unit

    cur.execute(''' SELECT dim_unit.id FROM "{}".public.dim_unit WHERE name_full= %s;'''.format(dbname),(unitName,))
    DBresponse = cur.fetchall()
    if len(DBresponse) == 0:
        cur.execute(''' SELECT max(id) FROM "{}".public.dim_unit'''.format(dbname))
        DBresponse = cur.fetchall()
        if DBresponse[0][0] == None:
            IDunit= 1
        else:
            IDunit = DBresponse[0][0] + 1
        cur.execute('''INSERT INTO public.dim_unit (id, name_short, name_full)
        VALUES (%s,%s,%s) ;''',(IDunit, unitName,unitName))
        connection.commit()
    else:
        IDunit = DBresponse[0][0]

##############open Excel

    try:
        wb = openpyxl.load_workbook(filename = '{}.xlsx'.format(ExcelName))
        sheet = wb.active
    except Exception as err: print(err)

############################insert values

    while rows_count <= rows_end:
        while columns_count <= columns_end:

###############Get ID fact

            cur.execute(''' SELECT max(id) FROM "{}".public.fact;'''.format(dbname))
            DBresponse = cur.fetchall()

            if DBresponse[0][0] != None:
                IDfact = DBresponse[0][0] + 1
            else:
                IDfact = 1

######################get values

            try:
                cell_value = GetValueOfArea.GetValueOfArea(sheet, columns_count ,rows_count)
            except Exception as err:
                error = True
                print('>>>>>>ERROR IN {} {}\nCan\'t Get Value'.format(cell_value, type(cell_value)),err)
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<')

######################values type inspection
            try: cell_value = str(cell_value)
            except Exception as err:
                    print('Can\'t string cell value {}'.format(cell_value), err)


            if len(cell_value) > 1 and cell_value != 'None':

                try: cell_value = cell_value.strip(' ')
                except: pass

                cellValueStateStarError = True

                while cellValueStateStarError == True:
                    if cell_value[-1] not in ['1','2','3','4','5','6','7','8','9','0']:
                        if len(cell_value) > 1:
                            cellValueStateStarError = True
                            cell_value = cell_value[:-1]
                        elif len(cell_value) == 1:
                            cellValueStateStarError = False
                    else: cellValueStateStarError = False

                try: cell_value = cell_value.replace(' ', '')
                except: pass

                try: cell_value = cell_value.replace(',','.')
                except : pass

            try: cell_value = float(cell_value)
            except: pass

            if type(cell_value) == float:

                try: cell_value = float(cell_value)
                except Exception as err:
                    error = True
                    print('>>>>>>ERROR IN {} {}'.format(cell_value, type(cell_value)))
                    print('>>>>>>Cell {} {} Error\nCan\'t Float\n'.format(columns_count,rows_count), err)
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<')

######################get value date and terr

                cell_date = str(GetValueOfArea.GetValueOfArea(sheet, columns_count, RowDate))

                if cell_date.count(' ') >= 1:
                    cell_date = cell_date.split(' ')
                    cell_date = cell_date[0]

                if cell_date.count('\\') >= 1:
                    cell_date = cell_date.split('\\')
                    cell_date = cell_date[0]

                if cell_date.count('/') >= 1:
                    cell_date = cell_date.split('/')
                    cell_date = cell_date[0]

                if cell_date.count('-') >= 1:
                    cell_date = cell_date.split('-')
                    cell_date = cell_date[0]

                cellValueStateStarError = True

                while cellValueStateStarError == True:
                    if cell_date[-1] not in ['1','2','3','4','5','6','7','8','9','0']:
                        cellValueStateStarError = True
                        cell_date = cell_date[:-1]
                    else: cellValueStateStarError = False

                cell_date = cell_date + '-01-01'

                cell_terr = str(GetValueOfArea.GetValueOfArea(sheet, ColumnTerrName, rows_count))
                cell_terr = cell_terr.strip(' ')

                if cell_terr == 'Мангыстауская':
                    cell_terr = 'Мангистауская'

                if cell_terr.count(' ') > 1:
                    spaceCount = cell_terr.count(' ')
                    cell_terr = cell_terr.replace(' '*spaceCount,' ')

                if cell_terr.count('г. ') >= 1:
                    cell_terr = cell_terr.split(' ')
                    cell_terr = cell_terr[0] + cell_terr[1]

##################### IDterr inspect

                try:
                    cur.execute("SELECT dim_terr.id FROM public.dim_terr WHERE territory_name = %s",(cell_terr,))
                    DBresponse = cur.fetchall()
                    IDterr = DBresponse[0][0]
                except Exception as err:
                    error = True
                    print('''>>>>>>>>>>Doesn\'t exist {} in cell row {} column {} in terr column {}. '
                          'Error '''.format(cell_terr, rows_count, columns_count, ColumnTerrName),err)
                    print(">>>>>>>>>>Pokazatel name  {}\nValue {}".format(IDpokazatel_name, cell_value))
                    print('>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<')

################insert value in cell


                if mode == 'addictive':
                    try:
                        cur.execute(''' INSERT INTO public.fact(id, id_date, id_terr, id_pokazatel, id_unit, value_additive)
                        VALUES (%s,%s,%s,%s,%s,%s); ''',(IDfact, cell_date, IDterr, IDpokazatel,IDunit,cell_value))
                        connection.commit()
                    except Exception as err:
                        error = True
                        print('>>>>>>>insert error {}'.format(type(cell_value)),err)
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                elif mode == 'avg':
                    try:
                        cur.execute(''' INSERT INTO public.fact(id, id_date, id_terr, id_pokazatel, id_unit, value_avg)
                        VALUES (%s,%s,%s,%s,%s,%s); ''',(IDfact, cell_date, IDterr, IDpokazatel,IDunit,cell_value))
                        connection.commit()
                    except Exception as err:
                        error = True
                        print('>>>>>>insert error',err)
                        print('>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<')

            elif type(cell_value) not in [float, int] and cell_value not in ['-','...','.','..']:
                print("+++++++++ Empty Cell\nValue {}\nType {}\nRow {} Column {}\nKategory {}\nName {} "
                          .format(cell_value,type(cell_value),rows_count,columns_count,pokazatelKetegory,IDpokazatel_name))
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            columns_count += 1
            IDfact += 1
        rows_count += 1

        columns_count = defaultColumnCount
    connection.close()
#Print results
    if error:
        print('=================================={}==========================\nError'.format(IDpokazatel_name))
        print('==============================================================')
    else:
        print('=================================={}==========================\nOK'.format(IDpokazatel_name))
        print('==============================================================')



