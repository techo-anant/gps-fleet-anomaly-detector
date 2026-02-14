import pytest
import pandas as pd
from analyzer import FleetAnalyzer

# Unit Testing
def test_speeding_detection():

    test_data = pd.DataFrame({
        'vehicle_id': ['ID-000', 'ID-001'],
        'speed_kmph': [90, 110],
        'harsh_brake_event': [True, False]
    })

    test_data.to_csv('test_data.csv', index=False)

    analyzer = FleetAnalyzer('test_data.csv')

    # for speeding tests
    speeding = analyzer.detect_speeding(threshold=100)

    assert len(speeding) == 1  
    assert speeding.iloc[0]['speed_kmph'] == 110

    # for break tests
    harsh_brake_count = analyzer.count_harsh_brake()

    assert harsh_brake_count['ID-000'] == 1
    assert harsh_brake_count['ID-001'] == 0
