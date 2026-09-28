def test_join_multi_levels(self):
    household = DataFrame(dict(household_id=[1, 2, 3], male=[0, 1, 0], wealth=[196087.3, 316478.7, 294750]), columns=['household_id', 'male', 'wealth']).set_index('household_id')
    portfolio = DataFrame(dict(household_id=[1, 2, 2, 3, 3, 3, 4], asset_id=['nl0000301109', 'nl0000289783', 'gb00b03mlx29', 'gb00b03mlx29', 'lu0197800237', 'nl0000289965', np.nan], name=['ABN Amro', 'Robeco', 'Royal Dutch Shell', 'Royal Dutch Shell', 'AAB Eastern Europe Equity Fund', 'Postbank BioTech Fonds', np.nan], share=[1.0, 0.4, 0.6, 0.15, 0.6, 0.25, 1.0]), columns=['household_id', 'asset_id', 'name', 'share']).set_index(['household_id', 'asset_id'])
    result = household.join(portfolio, how='inner')
    expected = DataFrame(dict(male=[0, 1, 1, 0, 0, 0], wealth=[196087.3, 316478.7, 316478.7, 294750.0, 294750.0, 294750.0], name=['ABN Amro', 'Robeco', 'Royal Dutch Shell', 'Royal Dutch Shell', 'AAB Eastern Europe Equity Fund', 'Postbank BioTech Fonds'], share=[1.0, 0.4, 0.6, 0.15, 0.6, 0.25], household_id=[1, 2, 2, 3, 3, 3], asset_id=['nl0000301109', 'nl0000289783', 'gb00b03mlx29', 'gb00b03mlx29', 'lu0197800237', 'nl0000289965'])).set_index(['household_id', 'asset_id']).reindex(columns=['male', 'wealth', 'name', 'share'])
    tm.assert_frame_equal(result, expected)
    result = merge(household.reset_index(), portfolio.reset_index(), on=['household_id'], how='inner').set_index(['household_id', 'asset_id'])
    tm.assert_frame_equal(result, expected)
    result = household.join(portfolio, how='outer')
    expected = concat([expected, DataFrame(dict(share=[1.0]), index=MultiIndex.from_tuples([(4, np.nan)], names=['household_id', 'asset_id']))], axis=0, sort=True).reindex(columns=expected.columns)
    tm.assert_frame_equal(result, expected)
    household.index.name = 'foo'
    with pytest.raises(ValueError):
        household.join(portfolio, how='inner')
    portfolio2 = portfolio.copy()
    portfolio2.index.set_names(['household_id', 'foo'])
    with pytest.raises(ValueError):
        portfolio2.join(portfolio, how='inner')