import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';
// import { YoutubeDlComponent } from "./youtube-dl.component";
import { SlideMenuComponent } from "./slide-menu.component";

declare var jQuery: any;

export class YouTubeLinking {
  link: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})

export class AppComponent implements AfterViewInit {

  @ViewChild('app-root') app: ElementRef;

  ngAfterViewInit() {
    jQuery('.tap-target').tapTarget('open');
  }

  youtubeLink: YouTubeLinking = {
    link: 'empty'
  };

}
