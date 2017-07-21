import { Component, ElementRef } from '@angular/core';
import { FileUploadService } from './file-upload.service';
import { Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';

@Component({
    selector: 'file-upload',
    templateUrl: './file-upload.component.html',
    providers: [ FileUploadService ]
})

export class FileUploadComponent {

    file: File;
    userAudio;
    isPlaying: false;

    constructor(private service: FileUploadService, private router: Router, private sanitizer: DomSanitizer) {
    }

    onChange(event) {
        console.log('fired');
        let files: FileList =  event.srcElement.files;
        this.file = files[0];
        this.userAudio = this.sanitize(URL.createObjectURL(this.file));
        // this.userAudio = this.sanitizer.bypassSecurityTrustResourceUrl(this.userAudio);
        console.log("userAudio: ", this.userAudio);
        this.service.uploadFile(this.file).subscribe((data) => {
            this.router.navigate(['/'])
        });
    }

    sanitize(url:string){
        return this.sanitizer.bypassSecurityTrustUrl(url);
    }
}
