import { Component, Injectable } from '@angular/core';
import { Http, Headers, Response, RequestOptions } from '@angular/http';


@Injectable()
export class YoutubeDlService {

    constructor(private http: Http) { }

    private headers = new Headers({'Content-Type': 'application/json'});

    public downloadYoutubeUrl(body: string) {
        console.log('youtube-dl.service url', body);
        return this.http.post('http://localhost:5000/api/youtube', body, {headers: this.headers});
    }
}