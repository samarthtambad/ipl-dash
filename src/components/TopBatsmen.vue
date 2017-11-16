<template>
  <div class="top-batsmen">
    <table class="table is-striped is-fullwidth">
        <thead>
        <tr>
            <th class="is-size-7" v-for="key in columns">
            {{ key | capitalize }}
            </th>
        </tr>
        </thead>
        <tbody>
            <tr class="is-size-7" v-for="entry in data">
                <td v-for="key in columns">
                    {{ entry[key] }}
                </td>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'TopBatsmen',
  props: {
    data: Array,
    columns: Array,
    filterKey: String
  },
  data: function () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  computed: {
    filteredData: function () {
      var data = this.data
      return data
    }
  },
  filters: {
    capitalize: function (str) {
      return str.charAt(0).toUpperCase() + str.slice(1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
