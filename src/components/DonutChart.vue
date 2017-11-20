<script>

import {Doughnut} from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: ['data', 'options', 'labels'],
  mounted () {
    this.renderDonutChart()
  },
  computed: {
    chartData: function() {
      console.log('computed')
      return this.data;
    }
  },
  methods: {
    renderDonutChart: function () {
      this.renderChart(
        {
          labels: this.labels,
          datasets: [
            {
              backgroundColor: [
                "#ED5F5A",
                "#70FFA0",
                "#CCCCCC",
                "#EA8CFF",
                "#47C2FF",
                "#F4F78F",
                "#4893B2",
                "#FECEB5",
                "#2B9E86",
                "#D38E7D",
                "#B1FFFF",
                "#A26B28",
                "#003468"
              ],
              cutoutPercentage: 0,
              label: "RCB",
              data: this.data
            }
          ]
        }, 
        {
          responsive: true,
          maintainAspectRatio: false,
          legend: {
            display: true,
            position: "right",
            labels: {
              boxWidth: 12,
              fontSize: 10,
              usePointStyle: true
            }
          }
        });
    }
  },
  watch: {
    data: function() {
      console.log(this)
      this.$data._chart.destroy()
      //this.renderChart(this.data, this.options);
      this.renderDonutChart()
    }
  }
}
</script>