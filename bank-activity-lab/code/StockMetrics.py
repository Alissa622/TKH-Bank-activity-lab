
import statistics as stats

from code.StockData import StockData


class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        
        
        averages = []
        for row in self.data:
            newrow= []
            for val in row[1:]:
                if val == " " or val == "": 
                    continue 
                else:
                    newrow.append(float(val))
            averages.append(round(sum(newrow)/len(newrow),3))


        return averages

    def median02(self):
        
        
        
        
        
        median = []
        for row in self.data:
            new_row = []
            for val in row[1:]:
                if val == " " or val == "":
                    continue
                else:
                    new_row.append(float(val))
            median.append(stats.median(new_row))
        return median

    def stddev03(self):
        
        
        stddev = []
        for row in self.data:
            new_row = []
            for val in row[1:]:
                if val == " " or val == "":
                    continue
                else:
                    new_row.append(float(val))
            stddev.append(round(stats.stdev(new_row),3))
        return stddev
        
