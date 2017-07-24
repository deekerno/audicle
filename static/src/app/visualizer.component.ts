import { Component, ViewChild, ElementRef, AfterViewInit } from '@angular/core';

var scene = document.querySelector('a-scene');
var sky = document.querySelector('a-sky');
var objectContainer = document.querySelector('#object-container');

@Component({
  selector: 'visualizer',
  templateUrl: './visualizer.component.html'
})

export class VisualizerComponent implements AfterViewInit {

  ngAfterViewInit() {
    // generateAllElements();
  }

  // random num generator
  getRandomNumber(x, y) {
      return Math.floor(Math.random() * x + y);
  }
  // get random hex color
  getRandomColor() {
      var letters = '0123456789abcdef';
      var randomColor = '';
      for (var i = 0; i < 6; i++) {
          randomColor += letters[Math.floor(Math.random() * 16)];
      }
      return randomColor;
  }


  // set sky values
//   sky.setAttribute('color', "#" + getRandomColor());
//   sky.setAttribute('animation__color', "property: color; dir: alternate; dur: 2000; easing: easeInOutSine; loop: true; to: #" + getRandomColor());
//   // change this value for more or less rings
//   var totalRingElements = 10;
//
//   generateAllElements() {
//       for (var a = 0; a < totalRingElements; a++) {
//           // element params
//           var totalCircleElements = getRandomNumber(10, 3);
//           var elementScale = getRandomNumber(3, 1);
//           var scaleDuration = getRandomNumber(3000, 1000);
//           // path params
//           var pathValOne = getRandomNumber(21, -10);
//           var pathValTwo = getRandomNumber(11, -20);
//           var pathDuration = getRandomNumber(6000, 5000);
//           for (var i = 1; i <= totalCircleElements; i++) {
//               var currentRotation = 360 / totalCircleElements * i;
//               var rotateContainer = document.createElement('a-entity');
//               rotateContainer.setAttribute('rotation', "0 0 " + currentRotation);
//               // generate circle element and set params
//               var circleElementContainer = document.createElement('a-entity');
//               circleElementContainer.setAttribute('position', "0 1 0");
//               var circleElement = document.createElement('a-entity');
//               circleElement.setAttribute('class', "circleElement");
//               circleElement.setAttribute('scale', elementScale + " " + elementScale + " " + elementScale);
//               circleElement.setAttribute('material', "color:#" + getRandomColor() + "; metalness: 0; roughness: 0");
//               circleElement.setAttribute('geometry', "primitive: sphere; radius: 1.5");
//               circleElement.setAttribute('animation__yoyo', "property: scale; dir: alternate; dur: " + scaleDuration + "; easing: easeInOutSine; loop: true; to: 0 0 0");
//               circleElementContainer.appendChild(circleElement);
//               rotateContainer.appendChild(circleElementContainer);
//               // generate path and apply it
//               var track1 = document.createElement('a-curve');
//               track1.setAttribute('class', "track" + a);
//               // scene.append(track1);
//               scene.appendChild(track1);
//               var point1 = document.createElement('a-curve-point');
//               point1.setAttribute('position', '0 0 0');
//               // track1.append(point1);
//               track1.appendChild(point1);
//               var point2 = document.createElement('a-curve-point');
//               point2.setAttribute('position', pathValOne + " " + pathValTwo + " " + pathValOne);
//               // track1.append(point2);
//               track1.appendChild(point2);
//               var point3 = document.createElement('a-curve-point');
//               point3.setAttribute('position', pathValTwo + " " + pathValOne + " " + pathValTwo);
//               // track1.append(point3);
//               track1.appendChild(point3);
//               var point4 = document.createElement('a-curve-point');
//               point4.setAttribute('position', '0 0 0');
//               // track1.append(point4);
//               track1.appendChild(point4);
//               circleElement.setAttribute("alongpath", "curve: .track" + a + "; dur: " + pathDuration + "; loop: true");
//               // append element to main container
//               objectContainer.appendChild(rotateContainer);
//           }
//       }
//   }
//
}
