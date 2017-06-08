import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { IGUsers } from "../models/igusers";
import { Observable } from "rxjs";
import 'rxjs/add/operator/map';

@Injectable()
export class IGUsersService {

  constructor (private http: Http) {}

  getUsers(): Observable<IGUsers[]> {
  	return this.http.get(`/api/users/`).map(res => res.json().data || {});
  }

  

}
