import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';

declare var jQuery: any;

@Component({
  selector: 'slide-menu',
  templateUrl: './slide-menu.component.html'
})

export class SlideMenuComponent implements AfterViewInit {
  @ViewChild('slide-menu') slideMenu: ElementRef;

  ngAfterViewInit() {
    jQuery(".button-collapse").sideNav();
  }
}
