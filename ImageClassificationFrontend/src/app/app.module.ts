import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';

import { IGUsersService } from "./igusers.service";
import { UserImagesComponent } from './user-images/user-images.component';

import { ChartsModule } from 'ng2-charts/ng2-charts';

@NgModule({
  declarations: [
    AppComponent,
    UserImagesComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ChartsModule
  ],
  providers: [
  	IGUsersService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
