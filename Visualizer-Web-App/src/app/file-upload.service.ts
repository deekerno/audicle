import { Injectable} from '@angular/core';
import { Http } from '@angular/http';


@Injectable()
export class FileUploadService {

    constructor(private http: Http) { }

    public uploadFile(body: File) {
        console.log('in FileUploadService ',body);
        return this.http.post('/api/upload', body);
    }
}