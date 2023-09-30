<template>
  <v-container>
    <v-row align="center" justify="center" style="margin-top: 55px;">
      <TopMenu />
    </v-row>
    <v-row >
    <Carousel />
    </v-row>
    <MainBanner />
    <SecondaryBanner />
    <v-container>
      <v-row >
        <DealsOfTheDay />
      </v-row>
    </v-container>
    <ShippingBanner />
  </v-container>
</template>

<script lang="ts" setup>
  import { ref } from 'vue';
  import TopMenu from '@/components/Home/TopMenu.vue';
  import Carousel from '@/components/Home/Carousel.vue';
  import MainBanner from '@/components/Home/MainBanner.vue';
  import SecondaryBanner from '@/components/Home/SecondaryBanner.vue';
  import ShoppingCategoriesBanner from '@/components/Home/SecondaryBanner.vue';

  import DealsOfTheDay from '@/components/Home/DealsOfTheDay';
  import ShippingBanner from '@/components/Home/ShippingBanner';

</script>
<style>
  .v-card--reveal {
    align-items: center;
    bottom: 0;
    justify-content: center;
    opacity: .5;
    position: absolute;
    width: 100%;
  }
</style>