import sys
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup")
sys.path.append("/home/stardust/A-Bare-Metal-Marketplace/database_setup/APIs")
sys.path.append("/home/stardust/A-Bare0Metal-Marketplace/database_setup/Models")
import data
import APIs.marketAPI as marketAPI
import Models.marketModel as Market
import pymysql


def test_bid_select_by_id():
    try:
        marketAPI.bid_insert(data.bid0)
    except Exception:
        print('inserted')
    finally:
        bid = marketAPI.bid_select_by_id(data.bid0['bid_id'])
        tmp = bid.__dict__
        del tmp['_sa_instance_state']
        assert tmp == data.bid0


def test_offer_select_by_id():
    try:
        marketAPI.offer_insert(data.offer0)
    except Exception:
        print('inserted')
    finally:
        offer = marketAPI.offer_select_by_id(data.offer0['offer_id'])
        tmp = offer.__dict__
        del tmp['_sa_instance_state']
        assert tmp == data.offer0


def test_bid_select_all():
    # marketAPI.offer_insert(data.bid0)
    marketAPI.bid_insert(data.bid1)
    results = marketAPI.bid_select_all()
    assert len(results) == 2
    row0 = results[0]
    tmp0 = row0.__dict__
    del tmp0['_sa_instance_state']
    assert tmp0 == data.bid0
    row1 = results[1]
    tmp1 = row1.__dict__
    del tmp1['_sa_instance_state']
    assert tmp1 == data.bid1


def test_offer_select_all():
    # marketAPI.offer_insert(data.bid0)
    marketAPI.offer_insert(data.offer1)
    results = marketAPI.offer_select_all()
    assert len(results) == 2
    row0 = results[0]
    tmp0 = row0.__dict__
    del tmp0['_sa_instance_state']
    assert tmp0 == data.offer1
    row1 = results[1]
    tmp1 = row1.__dict__
    del tmp1['_sa_instance_state']
    assert tmp1 == data.offer0


def test_bid_delete():
    marketAPI.bid_delete_by_id(data.bid0['bid_id'])
    results = marketAPI.bid_select_all()
    assert len(results) == 1
    row0 = results[0]
    tmp0 = row0.__dict__
    del tmp0['_sa_instance_state']
    assert tmp0 == data.bid1


def test_offer_delete():
    marketAPI.offer_delete_by_id(data.offer0['offer_id'])
    results = marketAPI.offer_select_all()
    assert len(results) == 1
    row0 = results[0]
    tmp0 = row0.__dict__
    del tmp0['_sa_instance_state']
    assert tmp0 == data.offer1
