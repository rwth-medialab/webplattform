<template>
  <div>
    <h3 class="form-subhead">Kompetenzen in der digitalen Welt</h3>
    <ul class="list-unstyled">
      <li class="form-check">
        <input class="form-check-input" type="checkbox" id="competence-1" name="competenceType" value="1" @change="update" v-model="internalCompetences">
        <label class="form-check-label" for="competence-1">Informieren & Recherchieren</label>
      </li>
      <li class="form-check">
        <input class="form-check-input" type="checkbox" id="competence-2" name="competenceType" value="2" @change="update" v-model="internalCompetences">
        <label class="form-check-label" for="competence-2">Kommunizieren & Kooperieren</label>
      </li>
      <li class="form-check">
        <input class="form-check-input" type="checkbox" id="competence-3" name="competenceType" value="3" @change="update" v-model="internalCompetences">
        <label class="form-check-label" for="competence-3">Produzieren & Präsentieren</label>
      </li>
      <li class="form-check">
        <input class="form-check-input" type="checkbox" id="competence-4" name="competenceType" value="4" @change="update" v-model="internalCompetences">
        <label class="form-check-label" for="competence-4">Bedienen & Anwenden</label>
      </li>
      <li class="form-check">
        <input class="form-check-input" type="checkbox" id="competence-5" name="competenceType" value="5" @change="update" v-model="internalCompetences">
        <label class="form-check-label" for="competence-5">Problemlösen & Modellieren</label>
      </li>
      <li class="form-check">
        <input class="form-check-input" type="checkbox" id="competence-6" name="competenceType" value="6" @change="update" v-model="internalCompetences">
        <label class="form-check-label" for="competence-6">Analysieren & Reflektieren</label>
      </li>
    </ul>
  </div>
</template>

<script>
  export default {
    name: 'CompetenceFilter',
    data () {
      return {
        internalCompetences: []
      }
    },
    props: {
      competences: {
        type: Array,
        default: () => {
          return []
        },
        required: false
      }
    },
    methods: {
      update () {
        this.$emit('update:competences', this.internalCompetences)
      }
    },
    created () {
      this.internalCompetences = this.competences
    }
  }
</script>

<style scoped>

</style>