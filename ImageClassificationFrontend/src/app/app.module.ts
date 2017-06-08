import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { IGUsersService } from "./igusers.service";

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
  	IGUsersService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
