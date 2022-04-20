from sqlalchemy import text


def test_get_goods_supplier_id(engine):

    data = []
    result = engine.execute(text("SELECT supplier_id  FROM goods WHERE id=1"))
    for row in result:
        data.append(row["supplier_id"])

    supplier_id_for_id_1 = data[0]
    expected_result = 9
    assert supplier_id_for_id_1 == expected_result


