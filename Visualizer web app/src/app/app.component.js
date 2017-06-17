"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var core_1 = require("@angular/core");
var UserInfo = (function () {
    function UserInfo() {
    }
    return UserInfo;
}());
exports.UserInfo = UserInfo;
var AppComponent = (function () {
    function AppComponent() {
        this.title = 'Music Visualizer';
        this.user = {
            id: 1,
            system: 'macOS'
        };
        this.canSave = true;
    }
    return AppComponent;
}());
AppComponent = __decorate([
    core_1.Component({
        selector: 'my-app',
        template: "\n    <h1 class = \"center-title\">{{title}}</h1>\n    <div id = \"footer\" class = \"center greyed-out\"> <button class = \"left-button\" [style.background-color]=\"canSave ? 'orange': 'grey'\" >Dislike</button>\n    <button class = \"right-button\">Like</button>\n    </div>\n  ",
    })
], AppComponent);
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map