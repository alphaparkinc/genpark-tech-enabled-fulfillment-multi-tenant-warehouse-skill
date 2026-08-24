from client import TechEnabledFulfillmentMultiTenantWarehouseClient

def main():
    client = TechEnabledFulfillmentMultiTenantWarehouseClient()
    res = client.allocate_on_demand_pallets('MERCH_RIYADH_02', 40, 'RIYADH_SOUTH_WAREHOUSE')
    print('Allocation: ' + res['allocation_id'] + ' at ' + res['warehouse_location'])
    print('Pallets: ' + str(res['pallets_allocated']) + ' @ $' + str(res['flexible_pay_as_you_store_rate_monthly_usd']) + '/mo')
    print('Same-Day SLA: ' + str(res['same_day_dispatch_sla_pct']) + '% | Courier Connected: ' + str(res['b2c_last_mile_courier_api_connected']))

if __name__ == '__main__':
    main()
