<template>
  <v-card outlined>
    <v-divider></v-divider>
    <v-card-title>Price</v-card-title>
    <v-range-slider
      v-model="range"
      :max="max"
      :min="min"
      :height="10"
      class="align-center"
      dense
    ></v-range-slider>
    <v-row class="pa-2" dense>
      <v-col cols="12" sm="5">
        <v-text-field
          :value="range[0]"
          label="Min"
          outlined
          dense
          @change="$set(range, 0, $event)"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="2">
        <p class="pt-2 text-center">TO</p>
      </v-col>
      <v-col cols="12" sm="5">
        <v-text-field
          :value="range[1]"
          label="Max"
          outlined
          dense
          @change="$set(range, 1, $event)"
        ></v-text-field>
      </v-col>
    </v-row>
    <v-divider></v-divider>
    <v-card-title class="pb-0">Customer Rating</v-card-title>
    <v-container class="pt-0"  fluid>
      <v-checkbox append-icon="mdi-star" label="4 & above" hide-details dense></v-checkbox>
      <v-checkbox append-icon="mdi-star" label="3 & above" hide-details dense></v-checkbox>
      <v-checkbox append-icon="mdi-star" label="2 & above" hide-details dense></v-checkbox>
      <v-checkbox append-icon="mdi-star" label="1 & above" hide-details dense></v-checkbox>
    </v-container>
    <v-divider></v-divider>
    <v-card-title class="pb-0">Size</v-card-title>
    <v-container class="pt-0" fluid>
      <v-checkbox  label="XS" hide-details dense></v-checkbox>
      <v-checkbox  label="S" hide-details dense></v-checkbox>
      <v-checkbox  label="M" hide-details dense></v-checkbox>
      <v-checkbox  label="L" hide-details dense></v-checkbox>
      <v-checkbox  label="XL" hide-details dense></v-checkbox>
      <v-checkbox  label="XXL" hide-details dense></v-checkbox>
      <v-checkbox  label="XXXL" hide-details dense></v-checkbox>
    </v-container>
  </v-card>
</template>


<script lang="ts" setup>
  import { ref } from 'vue';
  import FilterGroup from '@/components/Products/FilterGroup.vue';

  const range = ref([0, 10000]);
  const min = ref(0);
  const max = ref(10000);

</script>