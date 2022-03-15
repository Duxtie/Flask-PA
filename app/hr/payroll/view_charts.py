from flask_appbuilder.charts.views import DirectByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface

class CountryDirectChartView(DirectByChartView):
    datamodel = SQLAInterface(CountryStats)
    chart_title = 'Direct Data Example'

    definitions = [
    {
        'label': 'Unemployment',
        'group': 'stat_date',
        'series': ['unemployed_perc',
                   'college_perc']
    }
]