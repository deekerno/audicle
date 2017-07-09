import { Component } from '@angular/core';
// import { YoutubeDlComponent } from "./youtube-dl.component";

export class YouTubeLinking {
  link: string
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})

export class AppComponent {

  toggle = true;

  onClick() {
    this.toggle = !this.toggle;
  };

  youtubeLink: YouTubeLinking = {
    link: 'empty'
  };

}
