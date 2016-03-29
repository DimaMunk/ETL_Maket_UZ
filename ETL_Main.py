import ETL_modul_1

#Цены

ETL_modul_1.ExportInDB(unitName='Тенге',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Величина прожиточного минимума в среднем на душу населения',
                       rows_count=6,
                       columns_count=2,
                       rows_end=22,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=5,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение тарифов на перевозку грузов',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение тарифов на услуги почтовые курьерские и связи',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=10,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен оптовых продаж',
                       rows_count=6,
                       columns_count=2,
                       rows_end=22,
                       columns_end=2,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен оптовых продаж',
                       rows_count=27,
                       columns_count=2,
                       rows_end=43,
                       columns_end=2,
                       ColumnTerrName=1,
                       RowDate=24,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен оптовых продаж',
                       rows_count=66,
                       columns_count=2,
                       rows_end=82,
                       columns_end=2,
                       ColumnTerrName=1,
                       RowDate=63,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен оптовых продаж',
                       rows_count=105,
                       columns_count=2,
                       rows_end=121,
                       columns_end=2,
                       ColumnTerrName=1,
                       RowDate=102,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен оптовых продаж',
                       rows_count=144,
                       columns_count=2,
                       rows_end=160,
                       columns_end=2,
                       ColumnTerrName=1,
                       RowDate=141,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен оптовых продаж',
                       rows_count=183,
                       columns_count=2,
                       rows_end=199,
                       columns_end=2,
                       ColumnTerrName=1,
                       RowDate=180,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен предприятий производителей пром продукции',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен реализации продуктов сельского хозяйства',
                       rows_count=7,
                       columns_count=2,
                       rows_end=21,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=5,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен в стоительстве',
                       rows_count=6,
                       columns_count=2,
                       rows_end=22,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Цены',
                       IDpokazatel_name='Изменение цен на потребительские товары по регионам',
                       rows_count=6,
                       columns_count=2,
                       rows_end=22,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive')



#Уровень жизни и доходы населения

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Бедность',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=15,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Глубина бедности',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=15,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Глубина_Острота')



ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Острота бедности',
                       rows_count=5,
                       columns_count=16,
                       rows_end=21,
                       columns_end=29,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Глубина_Острота')


ETL_modul_1.ExportInDB(unitName='Тенге',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Денежные расходы домохозяйств',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=15,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Джини',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Джини',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=15,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Индекс реальных денежных доходов',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=15,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Ниже СПК',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=15,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Тенге',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Оценка номинальных денежных доходов. в среднем на душу',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=15,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='Оценка номинальных денежных доходов')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Оценка номинальных денежных доходов. к предыдущему году',
                       rows_count=4,
                       columns_count=16,
                       rows_end=20,
                       columns_end=29,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Оценка номинальных денежных доходов')

ETL_modul_1.ExportInDB(unitName='Тенге',
                       pokazatelKetegory='Уровень жизни и доходы населения',
                       IDpokazatel_name='Среднемесячная заработная плата по регионам',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=61,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

#Социальное обеспечение

ETL_modul_1.ExportInDB(unitName='Тенге',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Среднемесячный размер назначенной пенсии',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Человек',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Численность студ',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Тыс.человек',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Численность учащихся в дне',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число больничных коек',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число больничных организаций',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Человек',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число детей в дошкольных учреждениях',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число дневных общеобразова',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число зарегестрированных преступлений',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число колледжи_2011-12',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число постоянных дошкольных учреждений',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Число профессиональных школ_2011-12',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=11,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Количество вузов',
                       rows_count=4,
                       columns_count=2,
                       rows_end=13,
                       columns_end=20,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')


ETL_modul_1.ExportInDB(unitName='Человек',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Численность учащихся в колледжах',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Человек',
                       pokazatelKetegory='Социальное обеспечение',
                       IDpokazatel_name='Численность учащихся в профессиональных школах-лицеях',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=11,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')


#Реальный сектор экономики

ETL_modul_1.ExportInDB(unitName='Млн.тенге',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Валовая продукция 1990-2013',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=26,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Валовый сбор картофеля',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Валовый сбор масичных культур',
                       rows_count=5,
                       columns_count=2,
                       rows_end=19,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Валовый сбор овощей',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Валовый сбор сахарной свеклы',
                       rows_count=4,
                       columns_count=2,
                       rows_end=9,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Валовый сбор хлопка сырца',
                       rows_count=4,
                       columns_count=2,
                       rows_end=6,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Тыс.голов',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Верблюды',
                       rows_count=4,
                       columns_count=2,
                       rows_end=18,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Млн.тенге',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Инвестиции в основной капитал',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive')

ETL_modul_1.ExportInDB(unitName='Индекс',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Индексы промышленного производства. Итого по промышленности',
                       rows_count=6,
                       columns_count=3,
                       rows_end=22,
                       columns_end=27,
                       ColumnTerrName=28,
                       RowDate=4,
                       mode='avg',
                       ExcelName='Индексы промышленного производства по видам деятельности')

ETL_modul_1.ExportInDB(unitName='Индекс',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Индексы физического объема валовой продукции (услуг) сельского хозяйства',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=25,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='ИФО 1990-2014')

ETL_modul_1.ExportInDB(unitName='Индекс',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Индекс физического объема валовой продукции растениеводства',
                       rows_count=23,
                       columns_count=2,
                       rows_end=39,
                       columns_end=25,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='ИФО 1990-2014')

ETL_modul_1.ExportInDB(unitName='Индекс',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Индекс физического объема валовой продукции животноводства',
                       rows_count=41,
                       columns_count=2,
                       rows_end=57,
                       columns_end=25,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='ИФО 1990-2014')

ETL_modul_1.ExportInDB(unitName='Индекс',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Индекс физического объема услуг в области сельского хозяйства',
                       rows_count=59,
                       columns_count=2,
                       rows_end=75,
                       columns_end=25,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='ИФО 1990-2014')

ETL_modul_1.ExportInDB(unitName='Тыс.голов',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Численность крупного рогатого скота',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='КРС')

ETL_modul_1.ExportInDB(unitName='Тыс.голов',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Численность лошадей',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Лошади')

ETL_modul_1.ExportInDB(unitName='Тыс.тенге',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Объемы промышленного производства',
                       rows_count=6,
                       columns_count=2,
                       rows_end=22,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Объемы промышленного производства по видам экономической деятельности')

ETL_modul_1.ExportInDB(unitName='Тыс.голов',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Численность овец и коз',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Овцы и козы')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                       ' горнодобывающей промышленности и разработке'
                                       ' карьеров в Республике Казахстан. Уголь',
                       rows_count=6,
                       columns_count=2,
                       rows_end=16,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                       ' карьеров в Республике Казахстан. Нефть (включая газовый конденсант)',
                       rows_count=19,
                       columns_count=2,
                       rows_end=26,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                       ' карьеров в Республике Казахстан. Газ',
                       rows_count=47,
                       columns_count=2,
                       rows_end=54,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Руды железные',
                       rows_count=67,
                       columns_count=2,
                       rows_end=71,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                       ' карьеров в Республике Казахстан. Окатыши железорудные',
                       rows_count=74,
                       columns_count=2,
                       rows_end=75,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Руды медные',
                       rows_count=78,
                       columns_count=2,
                       rows_end=84,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Руды алюминиевые',
                       rows_count=87,
                       columns_count=2,
                       rows_end=88,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                       ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Свинец в свинцовом концентрате',
                       rows_count=91,
                       columns_count=2,
                       rows_end=95,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Цинк в цинковом концентрате',
                       rows_count=98,
                       columns_count=2,
                       rows_end=104,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                        ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Руды марганцевые',
                       rows_count=107,
                       columns_count=2,
                       rows_end=109,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                         ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Руды хромовые',
                       rows_count=112,
                       columns_count=2,
                       rows_end=113,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                         ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Соль и хлорид натрия чистый,  вода морская',
                       rows_count=116,
                       columns_count=2,
                       rows_end=129,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в'
                                         ' горнодобывающей промышленности и разработке'
                                        ' карьеров в Республике Казахстан. Асбест',
                       rows_count=132,
                       columns_count=2,
                       rows_end=133,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в горнодобывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Мясо и субпродукты пищевые',
                       rows_count=6,
                       columns_count=2,
                       rows_end=22,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Колбасы и изделия аналогичные из мяса',
                       rows_count=25,
                       columns_count=2,
                       rows_end=41,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.литров',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Соки фруктовые и овощные',
                       rows_count=44,
                       columns_count=2,
                       rows_end=60,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Масло растительное',
                       rows_count=63,
                       columns_count=2,
                       rows_end=77,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Маргарин и продукты аналогичные',
                       rows_count=80,
                       columns_count=2,
                       rows_end=86,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Молоко обработанное жидкое и сливки',
                       rows_count=89,
                       columns_count=2,
                       rows_end=105,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Молоко в твердой форме',
                       rows_count=108,
                       columns_count=2,
                       rows_end=118,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Масло сливочное',
                       rows_count=121,
                       columns_count=2,
                       rows_end=136,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Сыр и творог',
                       rows_count=139,
                       columns_count=2,
                       rows_end=155,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.сыр недозрелый или невыдержанный и творог',
                       rows_count=158,
                       columns_count=2,
                       rows_end=174,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.творог нежирный',
                       rows_count=177,
                       columns_count=2,
                       rows_end=193,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.творог жирный',
                       rows_count=196,
                       columns_count=2,
                       rows_end=210,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.сыры тертые, сыры в порошке, сыры голубые и сыры необработанные прочие, кроме сыра плавленного',
                       rows_count=213,
                       columns_count=2,
                       rows_end=225,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.сыры твердые',
                       rows_count=228,
                       columns_count=2,
                       rows_end=239,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.сыры мягкие',
                       rows_count=242,
                       columns_count=2,
                       rows_end=249,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей. Сыры рассольные.',
                       rows_count=252,
                       columns_count=2,
                       rows_end=261,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Сыр плавленный не тёртый и не в порошке',
                       rows_count=264,
                       columns_count=2,
                       rows_end=272,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.Продукты молочные прочие.',
                       rows_count=275,
                       columns_count=2,
                       rows_end=291,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'молоко и сливки сгущенные и с добавками или без добавок'
                                            ' сахара или других подслащивающих веществ, не в твердых формах',
                       rows_count=294,
                       columns_count=2,
                       rows_end=299,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'йогурт, молоко и сливки ферментированные или сквашенные прочие',
                       rows_count=302,
                       columns_count=2,
                       rows_end=318,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'кумыс',
                       rows_count=321,
                       columns_count=2,
                       rows_end=334,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'шубат',
                       rows_count=337,
                       columns_count=2,
                       rows_end=344,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'курт',
                       rows_count=347,
                       columns_count=2,
                       rows_end=353,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                           'Мука из культур зерновых и растительная',
                       rows_count=356,
                       columns_count=2,
                       rows_end=372,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Крупа, мука грубого помола и гранулы и продукты из культур зерновых прочие',
                       rows_count=375,
                       columns_count=2,
                       rows_end=387,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Хлеб свежий',
                       rows_count=473,
                       columns_count=2,
                       rows_end=489,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Сахар-сырец или сахар рафинированный',
                       rows_count=492,
                       columns_count=2,
                       rows_end=499,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Шоколад, изделия кондитерские из',
                       rows_count=518,
                       columns_count=2,
                       rows_end=534,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Макароны, лапша, кускус и изделия мучные аналогичные',
                       rows_count=537,
                       columns_count=2,
                       rows_end=553,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.литров',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Коньяк',
                       rows_count=556,
                       columns_count=2,
                       rows_end=561,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.литров',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Водка, спирт питьевой с содержанием спирта по объему менее 45,4%',
                       rows_count=564,
                       columns_count=2,
                       rows_end=580,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.литров',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Вино виноградное натуральное',
                       rows_count=583,
                       columns_count=2,
                       rows_end=598,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.литров',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Пиво, кроме осадков и отходов',
                       rows_count=601,
                       columns_count=2,
                       rows_end=617,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Млн.штук',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Сигары, черуты (сигары с обрезанными концами), сигарильи'
                                            ' (сигары тонкие), сигареты, папиросы из табака или его заменителей',
                       rows_count=620,
                       columns_count=2,
                       rows_end=626,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Шерсть (овечья) мытая обезжиренная или карбонизированная,'
                                            ' не подвергнутая кардо- и гребнечесанию',
                       rows_count=629,
                       columns_count=2,
                       rows_end=642,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Хлопок, кардо- и гребнечесаный',
                       rows_count=645,
                       columns_count=2,
                       rows_end=658,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.кв.м',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Ковры и изделия ковровые',
                       rows_count=661,
                       columns_count=2,
                       rows_end=671,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.кв.дц',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                           'Кожа из шкур скота крупного рогатого или шкур'
                                            ' животных семейства лошадиных без волосяного покрова',
                       rows_count=674,
                       columns_count=2,
                       rows_end=684,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.пар',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Обувь, кроме спортивной',
                       rows_count=687,
                       columns_count=2,
                       rows_end=703,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.пар',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Обувь с верхом из кожи, кроме спортивной обуви, обуви с'
                                           ' подноском защитным металлическим и обуви специальной разной',
                       rows_count=706,
                       columns_count=2,
                       rows_end=722,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.кв.м',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                            'Обувь с верхом из кожи, кроме спортивной обуви, обуви с'
                                           ' подноском защитным металлическим и обуви специальной разной',
                       rows_count=725,
                       columns_count=2,
                       rows_end=741,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей.'
                                           'Обувь с верхом из кожи, кроме спортивной обуви, обуви с'
                                           ' подноском защитным металлическим и обуви специальной разной',
                       rows_count=745,
                       columns_count=2,
                       rows_end=747,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')


ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Газойли (топливо дизельное)''',
                       rows_count=763,
                       columns_count=2,
                       rows_end=776,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Мазут топочный''',
                       rows_count=779,
                       columns_count=2,
                       rows_end=791,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Фосфор''',
                       rows_count=794,
                       columns_count=2,
                       rows_end=796,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Спирт этиловый''',
                       rows_count=799,
                       columns_count=2,
                       rows_end=810,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей. Удобрения азотные,'
                                            'минеральные или химические',
                       rows_count=813,
                       columns_count=2,
                       rows_end=820,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Удобрения фосфорные, минеральные или химические''',
                       rows_count=823,
                       columns_count=2,
                       rows_end=829,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Известь гашенная, негашеная и гидравлическая''',
                       rows_count=832,
                       columns_count=2,
                       rows_end=846,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Ферросплавы''',
                       rows_count=849,
                       columns_count=2,
                       rows_end=854,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Жесть белая и прокат листовой луженый''',
                       rows_count=857,
                       columns_count=2,
                       rows_end=858,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='кг',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Серебро аффинированное''',
                       rows_count=861,
                       columns_count=2,
                       rows_end=866,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='кг',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Золото необработанное и полуобработанное или в виде порошка''',
                       rows_count=869,
                       columns_count=2,
                       rows_end=879,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Алюминий необработанный; оксид алюминия''',
                       rows_count=882,
                       columns_count=2,
                       rows_end=890,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Свинец необработанный''',
                       rows_count=893,
                       columns_count=2,
                       rows_end=897,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Цинк необработанный''',
                       rows_count=900,
                       columns_count=2,
                       rows_end=902,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей. Медь рафинированная'
                                           ' необработанная, нелегированная',
                       rows_count=905,
                       columns_count=2,
                       rows_end=910,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Штук',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей. Приемники'
                                       ' телевизионные, объединенные или нет с приемниками радиовещательными или звуко-'
                                       ' или видеозаписывающей или  воспроизводящей аппаратурой',
                       rows_count=913,
                       columns_count=2,
                       rows_end=919,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Штук',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство продукции в обрабатывающей. Магнитофоны и'
                                                               ' аппаратура звукозаписывающая прочая',
                       rows_count=922,
                       columns_count=2,
                       rows_end=926,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Штук',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Автомобили легковые пассажирские''',
                       rows_count=929,
                       columns_count=2,
                       rows_end=931,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Штук',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Производство продукции в обрабатывающей. Автомобили легковые пассажирские''',
                       rows_count=934,
                       columns_count=2,
                       rows_end=943,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Производство продукции в обрабатывающей')

ETL_modul_1.ExportInDB(unitName='Тыс.голов',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Численность птицы''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Птицы')

ETL_modul_1.ExportInDB(unitName='Тыс.тенге',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Объем продукции (услуг) в лесном хозяйстве''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=10,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='рус_Лесное хозяйство')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Индекс физического объема продукции (услуг) лесного хозяйства''',
                       rows_count=25,
                       columns_count=2,
                       rows_end=41,
                       columns_end=10,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='рус_Лесное хозяйство')

ETL_modul_1.ExportInDB(unitName='Тыс.тенге',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Объем продукции (услуг) в рыболовстве и аквакультуре''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=10,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='рус_Рыбное хозяйство')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Индекс физического объема продукции (услуг) рыболовства и аквакультуры''',
                       rows_count=26,
                       columns_count=2,
                       rows_end=42,
                       columns_end=10,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='рус_Рыбное хозяйство')

ETL_modul_1.ExportInDB(unitName='Тыс.тонн',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Валовой сбор зерновых (включая рис) и бобовых культур''',
                       rows_count=5,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Сбор зерновых и бобовых культур')

ETL_modul_1.ExportInDB(unitName='Тыс.голов',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Свиньи''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Свиньи')

ETL_modul_1.ExportInDB(unitName='Млн.кВт.ч',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в секции электроснабжение, подачи газа,'
                                                        'пара и воздушного кондиционирования в Республике Казахстан.Электроэнергия',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Сектор D (Электроснабжение)')

ETL_modul_1.ExportInDB(unitName='Тыс.Гкал',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='Производство промышленной продукции в секции электроснабжение, подачи газа,'
                                                        'пара и воздушного кондиционирования в Республике Казахстан.Теплоэнергия',
                       rows_count=24,
                       columns_count=2,
                       rows_end=40,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Сектор D (Электроснабжение)')

ETL_modul_1.ExportInDB(unitName='Тыс.куб.м',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Сектор Е (Водоснабжение). Вода природная''',
                       rows_count=6,
                       columns_count=2,
                       rows_end=22,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Сектор Е (Водоснабжение)')

ETL_modul_1.ExportInDB(unitName='Тыс.куб.м',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Сектор Е (Водоснабжение). Вода питьевая''',
                       rows_count=25,
                       columns_count=2,
                       rows_end=41,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Сектор Е (Водоснабжение)')

ETL_modul_1.ExportInDB(unitName='Тыс.куб.м',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Сектор Е (Водоснабжение). Вода непитьевая''',
                       rows_count=44,
                       columns_count=2,
                       rows_end=60,
                       columns_end=26,
                       ColumnTerrName=27,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Сектор Е (Водоснабжение)')

ETL_modul_1.ExportInDB(unitName='Центнеров с одного гектара',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Уражайность масличных культур''',
                       rows_count=5,
                       columns_count=2,
                       rows_end=19,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='Уражайность масличных культур')

ETL_modul_1.ExportInDB(unitName='Центнеров с одного гектара',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Урожайность зерновых (включая рис) и бобовых культур''',
                       rows_count=5,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='Урожайность зернов-2')

ETL_modul_1.ExportInDB(unitName='Центнеров с одного гектара',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Урожайность картофеля''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='Урожайность Картофель')

ETL_modul_1.ExportInDB(unitName='Центнеров с одного гектара',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Урожайность овощей открытого грунта ''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=20,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='Урожайность овощей')

ETL_modul_1.ExportInDB(unitName='Центнеров с одного гектара',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Урожайность сахарной свеклы''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=9,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='Урожайность сахарной свеклы')

ETL_modul_1.ExportInDB(unitName='Центнеров с одного гектара',
                       pokazatelKetegory='Реальный сектор экономики',
                       IDpokazatel_name='''Урожайность хлопка-сырца''',
                       rows_count=4,
                       columns_count=2,
                       rows_end=6,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='avg',
                       ExcelName='Урожайность хлопка сырца')

########### Наука

ETL_modul_1.ExportInDB(unitName='Млн.тенге',
                       pokazatelKetegory='Наука',
                       IDpokazatel_name=' Внутренние затраты на научно-исследовательские и '
                                                                'опытно-конструкторские работы',
                       rows_count=5,
                       columns_count=3,
                       rows_end=21,
                       columns_end=14,
                       ColumnTerrName=2,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Затраты на НИОКР 2003-2014')


ETL_modul_1.ExportInDB(unitName='Млн.тенге',
                       pokazatelKetegory='Наука',
                       IDpokazatel_name='''Затраты на продуктовые и процессные инновации в промышленности''',
                       rows_count=11,
                       columns_count=2,
                       rows_end=27,
                       columns_end=12,
                       ColumnTerrName=1,
                       RowDate=10,
                       mode='addictive',
                       ExcelName='Затраты на продуктовые и процессные инновации')

ETL_modul_1.ExportInDB(unitName='Количество респондентов',
                       pokazatelKetegory='Наука',
                       IDpokazatel_name='''Инновационная активность предприятий''',
                       rows_count=6,
                       columns_count=3,
                       rows_end=22,
                       columns_end=14,
                       ColumnTerrName=2,
                       RowDate=5,
                       mode='addictive',
                       ExcelName='Инновационная активность предприятий')

ETL_modul_1.ExportInDB(unitName='Человек',
                       pokazatelKetegory='Наука',
                       IDpokazatel_name='''Численность персонала, занятого исследованиями и разработками по областям''',
                       rows_count=4,
                       columns_count=3,
                       rows_end=20,
                       columns_end=13,
                       ColumnTerrName=2,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Численность персонала занятого исследованиями 2004-2014')

ETL_modul_1.ExportInDB(unitName='Единиц',
                       pokazatelKetegory='Наука',
                       IDpokazatel_name=''' Число организаций, выполнявших исследования и разработки''',
                       rows_count=5,
                       columns_count=3,
                       rows_end=21,
                       columns_end=14,
                       ColumnTerrName=2,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Число организаций выполнывших исследования')

########## Заняттость населения

ETL_modul_1.ExportInDB(unitName='Тысяч человек',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Экономически активное население',
                       rows_count=6,
                       columns_count=6,
                       rows_end=22,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')

ETL_modul_1.ExportInDB(unitName='Тысяч человек',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Занятое население',
                       rows_count=28,
                       columns_count=6,
                       rows_end=44,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')

ETL_modul_1.ExportInDB(unitName='Тысяч человек',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Наемные работники',
                       rows_count=50,
                       columns_count=6,
                       rows_end=66,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')

ETL_modul_1.ExportInDB(unitName='Тысяч человек',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Самостоятельно занятые работники',
                       rows_count=72,
                       columns_count=6,
                       rows_end=88,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')


ETL_modul_1.ExportInDB(unitName='Тысяч человек',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Безработное население ',
                       rows_count=94,
                       columns_count=6,
                       rows_end=110,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')


ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Уровень безработицы',
                       rows_count=116,
                       columns_count=6,
                       rows_end=132,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Уровень молодежной безработицы (в возрасте 15-24 лет)',
                       rows_count=138,
                       columns_count=6,
                       rows_end=154,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')

ETL_modul_1.ExportInDB(unitName='Проценты',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Уровень молодежной безработицы (в возрасте 15-28 лет)',
                       rows_count=160,
                       columns_count=6,
                       rows_end=176,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')

ETL_modul_1.ExportInDB(unitName='Тысяч человек',
                       pokazatelKetegory='Занятость населения',
                       IDpokazatel_name='Основные индикаторы рынка труда.'
                                            'Экономически неактивное население ',
                       rows_count=182,
                       columns_count=6,
                       rows_end=198,
                       columns_end=72,
                       ColumnTerrName=1,
                       RowDate=4,
                       mode='addictive',
                       ExcelName='Основные индикаторы рынка труда1')

############### Внешняя торговля

ETL_modul_1.ExportInDB(unitName='Млн.долларов США',
                       pokazatelKetegory='Внешняя торговля',
                       IDpokazatel_name='Внешнеторговый оборот Республики Казахстан по регионам',
                       rows_count=5,
                       columns_count=2,
                       rows_end=21,
                       columns_end=17,
                       ColumnTerrName=1,
                       RowDate=3,
                       mode='addictive',
                       ExcelName='Внешнеторговый оборот по регионам2001-2014')