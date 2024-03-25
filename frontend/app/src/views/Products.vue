<template>
  <v-container>
    <v-row class="mt-12">
      <v-col md="3" sm="3" xs=12>
        <FilterGroup />
      </v-col>
      <v-col md="9" sm="9" xs="12">
        <v-breadcrumbs class="pb-0" :items="breadcrums"></v-breadcrumbs>
        <v-row dense>
          <v-col cols="12" sm="8" class="pl-6 pt-6">
            <small>Showing 1-12 of 200 products</small>
          </v-col>
          <v-col cols="12" sm="4">
            <v-select class="pb-5" v-model="select" :items="options" style="margin-bottom: -20px;" outlined dense></v-select>
          </v-col>
        </v-row>

        <v-divider></v-divider>

        <v-row class="text-center">
          <v-col cols="12" md="3" sm="6" xs="12"
            :key="prod.id" v-for="prod in products">
            <ProductCard :product="prod" />
          </v-col>
        </v-row>
        <div class="text-center mt-12">
          <v-pagination
            v-model="page"
            :length="6"
            elevation="2"
          ></v-pagination>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<style>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .8;
    position: absolute;
    width: 100%;
  }
</style>

<script lang="ts" setup>
  import { ref } from 'vue';
  import FilterGroup from '@/components/Products/FilterGroup.vue';
  import ProductCard from '@/components/Products/ProductCard.vue';

  const select = ref('Popularity');
  const options = ref([
                'Default',
                'Popularity',
                'Relevance',
                'Price: Low to High',
                'Price: High to Low',
            ]);
  const page = ref(1);
  const breadcrumbs = ref([
        {
            text: 'Home',
            disabled: false,
            href: 'breadcrumbs_home',
        },
        {
            text: 'Clothing',
            disabled: false,
            href: 'breadcrumbs_clothing',
        },
        {
            text: 'T-Shirts',
            disabled: true,
            href: 'breadcrumbs_shirts',
        },
  ]);
  const items = ref([
      {
          id: 2,
          name: 'Shoes',
          children: [
              { id: 2, name: 'Casuals' },
              { id: 3, name: 'Formals' },
              { id: 4, name: 'Sneakers' },
          ],
      },
      {
          id: 1,
          name: 'Clothing',
          children: [
              { id: 5, name: 'Shirts' },
              { id: 6, name: 'Tops' },
              { id: 7, name: 'Tunics' },
              { id: 8, name: 'Bodysuit' },
          ],
      }
  ]);
  const products = ref([
    {
        id:1,
        name:'BLACK TEE',
        type:'Jackets',
        price:'18.00',
        src: 'https://loving-leavitt-9cb65b.netlify.app/static/img/1.60540e6.jpg'
    },
    {
        id:2,
        name:'WHITE TEE',
        type:'Polo',
        price:'40.00',
        src: '../assets/img/shop/2.jpg'
    },
    {
        id:3,
        name:'Zara limited...',
        type:'Denim',
        price:'25.00',
        src: '../assets/img/shop/3.jpg'
    },
    {
        id:4,
        name:'SKULL TEE',
        type:'Jackets',
        price:'30.00',
        src: '/assets/img/shop/4.jpg'
    },
    {
        id:5,
        name:'MANGO WINTER',
        type:'Sweaters',
        price:'50.00',
        src: '/assets/img/shop/5.jpg'
    },
    {
        id:6,
        name:'SHIRT',
        type:'Denim',
        price:'34.00',
        src: '../assets/img/shop/6.jpg'
    },
    {
        id:7,
        name:'TRUCKER JACKET',
        type:'Jackets',
        price:'38.00',
        src: '../assets/img/shop/7.jpg'
    },
    {
        id:8,
        name:'COATS',
        type:'Jackets',
        price:'25.00',
        src: '../assets/img/shop/8.jpg'
    },
    {
        id:9,
        name:'MANGO WINTER',
        type:'Sweaters',
        price:'50.00',
        src: '../assets/img/shop/9.jpg'
    },
    {
        id:10,
        name:'SHIRT',
        type:'Denim',
        price:'34.00',
        src: '/assets/img/shop/10.jpg'
    },
    {
        id:11,
        name:'TRUCKER JACKET',
        type:'Jackets',
        price:'38.00',
        src: '/assets/img/shop/11.jpg'
    },
    {
        id:12,
        name:'COATS',
        type:'Jackets',
        price:'25.00',
        src:'../assets/img/shop/12.jpg'
    }
  ]);

</script>