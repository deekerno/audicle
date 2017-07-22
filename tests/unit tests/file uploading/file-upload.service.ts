import { Injectable} from '@angular/core';
import { Http, Headers } from '@angular/http';


@Injectable()
export class FileUploadService {

    private headers = new Headers({'Content-Type': 'application/json'});

    private url = "http://localhost:5000/upload"

    constructor(private http: Http) { }

    public uploadFile(body: File) {
        console.log('in FileUploadService ',body);
        return this.http.post(this.url, body, {headers: this.headers});
    }
}