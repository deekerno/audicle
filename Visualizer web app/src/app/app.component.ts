import { Component } from '@angular/core';


export class UserInfo {
  id: number;
  system: string
}


@Component({
  selector: 'my-app',
  template: `
    <h1 class = "center-title">{{title}}</h1>
    <div id = "footer" class = "center greyed-out"> <button class = "left-button" [style.background-color]="canSave ? 'orange': 'grey'" >Dislike</button>
    <button class = "right-button">Like</button>
    </div>
  `,
})

export class AppComponent {
  title = 'Music Visualizer';
  user: UserInfo = {
    id: 1,
    system: 'macOS'
  };
  canSave = true;
}
