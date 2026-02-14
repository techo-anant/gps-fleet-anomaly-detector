import pandas as pd

class FleetAnalyzer:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

    def detect_speeding( self, threshold=100):
        return self.df[self.df['speed_kmph'] > threshold]
    
    def count_harsh_brake( self ):
        return self.df.groupby('vehicle_id')['harsh_brake_event'].sum()
    
    def generate_health_report( self ):
        report = {
            'num_vehicle': self.df['vehicle_id'].nunique(),
            'speeding_events': len(self.detect_speeding()),
            'harsh_brakes_by_vehicle': self.count_harsh_brake().to_dict()
        }
        
        return report

if __name__ == '__main__':
    analyzer = FleetAnalyzer('fleet_data.csv')
    print(analyzer.generate_health_report())
