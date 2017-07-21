import { Component, ElementRef } from '@angular/core';
import { FileUploadService } from './file-upload.service';
import { Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';
import { AudioPlayerService } from './audio-player.service';

@Component({
    selector: 'file-upload',
    templateUrl: './file-upload.component.html',
    providers: [ FileUploadService, AudioPlayerService ]
})

export class FileUploadComponent {

    private file: File;
    private song;

    constructor(private UploadService: FileUploadService, private router: Router, private sanitizer: DomSanitizer, private AudioService: AudioPlayerService) {
        this.song = this.AudioService.userAudio;
    }

    onChange(event) {
        let files: FileList =  event.srcElement.files;
        this.file = files[0];
        this.song = this.sanitize(URL.createObjectURL(this.file));
        this.sendFile(this.song);
    }

    sanitize(url:string){
        return this.sanitizer.bypassSecurityTrustUrl(url);
    }

    sendFile(song) {
        console.log('fired');
        this.UploadService.uploadFile(song).subscribe((data) => {
            this.router.navigate(['/'])
        });
    }
}
