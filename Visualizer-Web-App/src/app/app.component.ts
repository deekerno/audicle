import { Component } from '@angular/core';
// import { YoutubeDlComponent } from "./youtube-dl.component";
import { SlideMenuComponent } from "./slide-menu.component";

export class YouTubeLinking {
  link: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})

export class AppComponent {

  youtubeLink: YouTubeLinking = {
    link: 'empty'
  };

}
