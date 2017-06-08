import { Component, OnInit, Input } from '@angular/core';
import { IGUsersService } from "../igusers.service";
import { IGUsers } from '../../models/igusers'
import { Observable } from "rxjs";

@Component({
  selector: 'app-user-images',
  templateUrl: './user-images.component.html',
  styleUrls: ['./user-images.component.css']
})
export class UserImagesComponent implements OnInit {

	@Input() user: IGUsers;
	userDetails: Observable<any>;

	constructor(private igusersService: IGUsersService) { }

	ngOnInit() {
		this.userDetails = this.igusersService.getDetails(this.user);

		this.userDetails.subscribe(x => console.log(x));
	}

}
