import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { IGUsers } from "../models/igusers";
import { Observable } from "rxjs";
import 'rxjs/add/operator/map';

@Injectable()
export class IGUsersService {

  constructor (private http: Http) {}

  getUsers(): Observable<IGUsers[]> {
  	return this.http.get(`/api/users/`).map(res => res.json());
  }

  getDetails(user: IGUsers) {
  	return this.http.get(`/api/users/${user.uid}/tags/details/`).map(res => res.json());
  }

  processUser(handle: string) {
  	// TODO
  }

  getAllTags() {
    return this.http.get(`/api/data/tags`).map(res => res.json());
  }

  getTagSumValues() {
    return this.http.get(`/api/data/sumvalues`).map(res => res.json());
  }

  getTagMeanValues() {
    return this.http.get(`/api/data/meanvalues`).map(res => res.json());
  }

}
