<template>
  <div class="table-element">
    <table class="table is-striped is-fullwidth">
        <thead>
        <tr>
            <th class="is-size-7" v-for="key in columns">
            {{ key }}
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
  name: 'TableElement',
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
    
  },
  filters: {
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
