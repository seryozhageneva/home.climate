import sqlite3


def create_table():
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS links (
                        photo_path TEXT,
                        name TEXT,
                        square TEXT,
                        house_type TEXT,
                        price_category TEXT,
                        price REAL,
                        article TEXT,
                        link TEXT)''')
    conn.commit()
    conn.close()


def insert_data(data):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM links")

    cursor.executemany(
        "REPLACE INTO links (photo_path, name, square, house_type, price_category, price, article, link) VALUES (?, "
        "?, ?, ?, ?, ?, ?, ?)",
        data)

    conn.commit()
    conn.close()


def get_links(square, house_type, price_category):
    conn = sqlite3.connect('links.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT link FROM links WHERE square = ? AND house_type = ? AND price_category = ?''',
                   (square, house_type, price_category))
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]


create_table()

data = [
    # 1
    ('images/conditioner1.jpg', 'Бирюса B-07FPR/B-07FPQ', 'До 18 кв.м.', 'On/Off', 'Бюджет', '16 700', '1001',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=929&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner2.jpg', 'Berlingtoun BR-07MBST1', 'До 18 кв.м.', 'On/Off', 'Бюджет', '18 800', '1002',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=953&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner3.jpg', 'Roland 07 on/off', 'До 18 кв.м.', 'On/Off', 'Бюджет', '19 000', '1003',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=613&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 2
    ('images/conditioner4.jpg', 'Daichi DA20EVQ1-1-DF20EV1-1', 'До 18 кв.м.', 'On/Off', 'Стандарт', '25 000', '1004',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=875&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner5.jpg', 'Gree Bora 07 on/off', 'До 18 кв.м.', 'On/Off', 'Стандарт', '25 500', '1005',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=284&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner6.jpg', 'Lessar Cool+ 07 on/off', 'До 18 кв.м.', 'On/Off', 'Стандарт', '25 500', '1006',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=262&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 3
    ('images/conditioner7.jpg', 'Electrolux Portofino 07 on/off', 'До 18 кв.м.', 'On/Off', 'Премиум', '28 200', '1007',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=765&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner8.jpg', 'Tosot T07H-SnN2/I/T07H-SnN2/O', 'До 18 кв.м.', 'On/Off', 'Премиум', '28 500', '1008',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=675&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner9.jpg', 'Haier Lightera on/off 07', 'До 18 кв.м.', 'On/Off', 'Премиум', '30 900', '1009',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=96&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 4
    ('images/conditioner10.jpg', 'Бирюса B-07FIR/B-07FIQ', 'До 18 кв.м.', 'Инвертор', 'Бюджет', '23 500', '1010',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=978&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner11.jpg', 'Бирюса B-07EIR/B-07EIQ', 'До 18 кв.м.', 'Инвертор', 'Бюджет', '25 600', '1011',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=989&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner12.jpg', 'Berlingtoun BR-07MBIN1', 'До 18 кв.м.', 'Инвертор', 'Бюджет', '26 000', '1012',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=956&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 5
    ('images/conditioner13.jpg', 'Tosot Lyra 07 Inverter', 'До 18 кв.м.', 'Инвертор', 'Стандарт', '37 200', '1013',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=784&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner14.jpg', 'Haier AS07TT4HRA/1U07TL5RA', 'До 18 кв.м.', 'Инвертор', 'Стандарт', '37 700', '1014',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=935&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner15.jpg', 'Haier AS20HPL1HRA/1U20HPL1FRA', 'До 18 кв.м.', 'Инвертор', 'Стандарт', '42 600',
     '1015',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=918&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 6
    ('images/conditioner16.jpg', 'Panasonic CS/CU-PZ20WKD', 'До 18 кв.м.', 'Инвертор', 'Премиум', '60 500', '1016',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=921&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner17.jpg', 'Panasonic CS-TZ20WKEW', 'До 18 кв.м.', 'Инвертор', 'Премиум', '81 500', '1017',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=948&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner18.jpg', 'Daikin Invertor Sensira FTXF20B/RXF20B', 'До 18 кв.м.', 'Инвертор', 'Премиум',
     '104 500', '1018',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=591&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2018%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 7
    ('images/conditioner19.jpg', 'Бирюса B-09FPR/B-09FPQ', 'До 28 кв.м.', 'On/Off', 'Бюджет', '17 900', '1019',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=930&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner20.jpg', 'Roland 09 on/off', 'До 28 кв.м.', 'On/Off', 'Бюджет', '20 500', '1020',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=614&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner21.jpg', 'Berlingtoun BR-09MBST1', 'До 28 кв.м.', 'On/Off', 'Бюджет', '20 800', '1021',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=954&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 8
    ('images/conditioner22.jpg', 'Midea MSAG3-09HRN1-I', 'До 28 кв.м.', 'On/Off', 'Стандарт', '25 800', '1022',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=926&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner23.jpg', 'Haier HSU-09HPL103/R3', 'До 28 кв.м.', 'On/Off', 'Стандарт', '26 000', '1023',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=912&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner24.jpg', 'Kentatsu KSGTI26HFAN1', 'До 28 кв.м.', 'On/Off', 'Стандарт', '26 000', '1024',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=987&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 9
    ('images/conditioner25.jpg', 'Electrolux Portofino 09', 'До 28 кв.м.', 'On/Off', 'Премиум', '31 000', '1025',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=766&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner26.jpg', 'Tosot T09H-SnN2/I/T09H-SnN2/O', 'До 28 кв.м.', 'On/Off', 'Премиум', '31 400', '1026',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=676&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner27.jpg', 'Haier Lightera 09', 'До 28 кв.м.', 'On/Off', 'Премиум', '33 300', '1027',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=97&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 10
    ('images/conditioner28.jpg', 'Бирюса B-09DIR/B-09DIQ', 'До 28 кв.м.', 'Инвертор', 'Бюджет', '25 500', '1028',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=979&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner29.jpg', 'Бирюса B-09EIR/B-09EIQ', 'До 28 кв.м.', 'Инвертор', 'Бюджет', '27 700', '1029',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=990&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner30.jpg', 'Roland 09 Invertor', 'До 28 кв.м.', 'Инвертор', 'Бюджет', '28 200', '1030',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=759&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 11
    ('images/conditioner31.jpg', 'Gree GWH09ACC-K6DNA1F Black', 'До 28 кв.м.', 'Инвертор', 'Стандарт', '58 300', '1031',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=951&mfp=12-kvadratura-komnaty%5B%D0%B4%D0'
     '%BE%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner32.jpg', 'LG ProCool Inverter 09', 'До 28 кв.м.', 'Инвертор', 'Стандарт', '61 000', '1032',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=782&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner33.jpg', 'Panasonic CS/CU-PZ25WKD', 'До 28 кв.м.', 'Инвертор', 'Стандарт', '64 200', '1033',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=886&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 12
    ('images/conditioner34.jpg', 'Haier AS25S2SF2FA-W/G/B', 'До 28 кв.м.', 'Инвертор', 'Премиум', '88 900', '1034',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=938&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner35.jpg', 'Daikin Invertor Sensira FTXF25B/RXF25B', 'До 28 кв.м.', 'Инвертор', 'Премиум',
     '107 000', '1035',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=592&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner36.jpg', 'LG A09FT ARTCOOL Gallery Inverter', 'До 28 кв.м.', 'Инвертор', 'Премиум', '147 500',
     '1036',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=888&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2028%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 13
    ('images/conditioner37.jpg', 'Бирюса B-12DPR/B-12DPQ', 'До 38 кв.м.', 'On/Off', 'Бюджет', '22 800', '1037',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=931&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner38.jpg', 'Roland 12 on/off', 'До 38 кв.м.', 'On/Off', 'Бюджет', '26 200', '1038',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=615&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner39.jpg', 'Berlingtoun BR-12MBST1', 'До 38 кв.м.', 'On/Off', 'Бюджет', '26 800', '1039',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=955&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 14
    ('images/conditioner40.jpg', 'Kentatsu KSGTI35HFAN1', 'До 38 кв.м.', 'On/Off', 'Стандарт', '32 300', '1040',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=988&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner41.jpg', 'Daichi DA35EVQ1-1-DF35EV1-1', 'До 38 кв.м.', 'On/Off', 'Стандарт', '33 500', '1041',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=877&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner42.jpg', 'Lessar Cool+ 12', 'До 38 кв.м.', 'On/Off', 'Стандарт', '33 800', '1042',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=264&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 15
    ('images/conditioner43.jpg', 'Green 12 HH2', 'До 38 кв.м.', 'On/Off', 'Премиум', '37 000', '1043',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=872&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner44.jpg', 'Gree Pular 12 on/off', 'До 38 кв.м.', 'On/Off', 'Премиум', '37 500', '1044',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=797&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),
    ('images/conditioner45.jpg', 'Haier Lightera on/off 12', 'До 38 кв.м.', 'On/Off', 'Премиум', '37 600', '1045',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=98&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5BonLw%3D%3Doff%5D'),

    # 16
    ('images/conditioner46.jpg', 'Бирюса B-12DIR/B-12DIQ', 'До 38 кв.м.', 'Инвертор', 'Бюджет', '28 000', '1046',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=980&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner47.jpg', 'AUX ASW-H07A4/FP-R1DI', 'До 38 кв.м.', 'Инвертор', 'Бюджет', '29 000', '1047',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=971&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner48.jpg', 'AUX ASW-H09A4/FP-R1DI', 'До 38 кв.м.', 'Инвертор', 'Бюджет', '30 500', '1048',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=972&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 17
    ('images/conditioner49.jpg', 'Gree Bora Inverter GWH12AABXB-K6DNA2C', 'До 38 кв.м.', 'Инвертор', 'Стандарт',
     '55 300', '1049',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=661&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner50.jpg', 'Gree GWH12ACC-K6DNA1F Black', 'До 38 кв.м.', 'Инвертор', 'Стандарт', '65 500', '1050',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=952&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner51.jpg', 'LG ProCool Inverter 12', 'До 38 кв.м.', 'Инвертор', 'Стандарт', '69 000', '1051',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=783&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),

    # 18
    ('images/conditioner52.jpg', 'Haier AS35S2SF2FA-W/G/B', 'До 38 кв.м.', 'Инвертор', 'Премиум', '101 200', '1052',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=939&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner53.jpg', 'Daikin Invertor Sensira FTXF35A/RXF35A', 'До 38 кв.м.', 'Инвертор', 'Премиум',
     '123 000', '1053',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=593&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D'),
    ('images/conditioner54.jpg', 'LG A12FT ARTCOOL Gallery Inverter', 'До 38 кв.м.', 'Инвертор', 'Премиум', '159 000',
     '1054',
     'https://xn----7sbbnvbfjjehfk1e3d.xn--p1ai/kondicionery?product_id=889&mfp=12-kvadratura-komnaty%5B%D0%B4%D0%BE'
     '%2038%20%D0%BA%D0%B2.%D0%BC.%5D%2C13-tip-kompressora%5B%D0%B8%D0%BD%D0%B2%D0%B5%D1%80%D1%82%D0%BE%D1%80%5D')
]

insert_data(data)
