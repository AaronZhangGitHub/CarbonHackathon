import { TestBed, inject } from '@angular/core/testing';

import { IGUsersService } from './igusers.service';

describe('IGUsersService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [IGUsersService]
    });
  });

  it('should be created', inject([IGUsersService], (service: IGUsersService) => {
    expect(service).toBeTruthy();
  }));
});
