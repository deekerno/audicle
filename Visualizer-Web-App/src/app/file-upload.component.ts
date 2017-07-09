import { Component, ElementRef } from '@angular/core';
import { FileUploadService } from './file-upload.service';
import { Router } from '@angular/router';

@Component({
    selector: 'file-upload',
    templateUrl: './file-upload.component.html',
    providers: [ FileUploadService, ]
})

export class FileUploadComponent {

    file: File;

    constructor(private service: FileUploadService, private router: Router) {
    }

    onChange(event) {
        console.log('fired');
        let files: FileList =  event.srcElement.files;
        this.file = files[0];
        this.service.uploadFile(this.file).subscribe((data) => {
            this.router.navigate(['/'])
        });
    }
}
