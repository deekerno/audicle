import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { YoutubeDlComponent } from './youtube-dl.component';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { HttpModule } from "@angular/http";
import { RouterModule } from "@angular/router";
import { ROUTES } from './app.routes'
import { SlideMenuComponent } from "./slide-menu.component"

@NgModule({
  declarations: [
    AppComponent,
    YoutubeDlComponent,
    SlideMenuComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    RouterModule.forRoot(ROUTES)
  ],
  providers: [],
  bootstrap: [AppComponent, YoutubeDlComponent, SlideMenuComponent]
})
export class AppModule { }
