import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { YoutubeDlComponent } from './youtube-dl.component';
import { FileUploadComponent } from './file-upload.component';
import { FormsModule, ReactiveFormsModule } from "@angular/forms";
import { HttpModule } from "@angular/http";
import { RouterModule } from "@angular/router";
import { ROUTES } from './app.routes'
import { SlideMenuComponent } from "./slide-menu.component"
import { VisualizerComponent } from "./visualizer.component";
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';

@NgModule({
  declarations: [
    AppComponent,
    YoutubeDlComponent,
    SlideMenuComponent,
    FileUploadComponent,
    VisualizerComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpModule,
    RouterModule.forRoot(ROUTES),
  ],
  providers: [],
  bootstrap: [AppComponent, YoutubeDlComponent, SlideMenuComponent, VisualizerComponent, ],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})

export class AppModule { }
