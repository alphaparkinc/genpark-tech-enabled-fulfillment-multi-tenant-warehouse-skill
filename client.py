class TechEnabledFulfillmentMultiTenantWarehouseClient:
    def allocate_on_demand_pallets(self, merchant_id='MERCH_CAIRO_09', pallet_count_needed=25, market_region='EGYPT_GIZA_HUB'):
        return {
            'allocation_id': 'flx_alc_88124',
            'merchant_id': merchant_id,
            'warehouse_location': market_region,
            'pallets_allocated': pallet_count_needed,
            'flexible_pay_as_you_store_rate_monthly_usd': round(pallet_count_needed * 18.5, 2),
            'same_day_dispatch_sla_pct': 99.1,
            'b2c_last_mile_courier_api_connected': True
        }
