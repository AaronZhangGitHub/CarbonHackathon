import { Component, OnInit } from '@angular/core';
import { IGUsers } from "../models/igusers";
import { IGUsersService } from "./igusers.service";
import { Observable } from "rxjs";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
	searchUserName: string;

	users: Observable<IGUsers[]>;
	selectedUser: IGUsers;

	tags: Observable<string[]>;
	sums: Observable<number[]>;
	means: Observable<number[]>;

	constructor (private igusersService: IGUsersService) { }
  
	ngOnInit() {
		this.users = this.igusersService.getUsers();
		this.tags = this.igusersService.getAllTags();
		this.sums = this.igusersService.getTagSumValues();
		this.means = this.igusersService.getTagMeanValues();
	}

	select(user: IGUsers) {
		this.selectedUser = user;
	}

	unselect() {
		this.selectedUser = null;
	}

	search() {
		this.igusersService.processUser(this.searchUserName);
	}

}
