<template>
  <v-row class="pl-4 pr-4">
    <v-col md="6" sm="6" xs="12">
      <v-card>
        <v-img
          src="@/assets/img/home/slider2.jpg"
          class="white--text align-center"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          height="400px"
        >
         <h1 class="text-center font-size">Top Picks</h1>
          <div class="text-center">
            <v-btn  href="/shop" class="white--text " outlined>SHOP NOW</v-btn>
          </div>
    <!--            <v-expand-transition>-->
    <!--              <div-->
    <!--                v-if="hover"-->
    <!--                class="d-flex transition-fast-in-fast-out orange darken-2 v-card&#45;&#45;reveal display-3 white&#45;&#45;text"-->
    <!--                style="height: 100%;"-->
    <!--              >-->

    <!--                <h3>Top Picks</h3><br/>-->
    <!--                <h3>sdfs</h3>-->
    <!--              </div>-->
    <!--            </v-expand-transition>-->
        </v-img>
      </v-card>
    <!--        </v-hover>-->
    </v-col>
    <v-col md="6" sm="6" xs="12">
      <v-card>
        <v-img
          src="@/assets/img/home/slider3.jpg"
          class="white--text align-center"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
          height="400px"
        >
          <h1 class="text-center font-size">New Arrivals</h1>
          <div class="text-center">
            <v-btn  href="/shop" class="white--text" outlined>SHOP NOW</v-btn>
          </div>
        </v-img>
      </v-card>
    </v-col>
  </v-row>
</template>
