import { Component, OnInit } from '@angular/core';
import { Fortune } from 'app/models/fortune';

import { FortuneService } from 'app/services/fortune.service';
import { MessageService } from 'app/services/message.service';

@Component({
  selector: 'app-cookies',
  templateUrl: './cookies.component.html',
  styleUrls: ['./cookies.component.css']
})
export class CookiesComponent implements OnInit {
  selectedFortune: Fortune;
  cookieImage: string;
  changeText: string;
  showMessage: boolean;
  cookieOpened: boolean;
  messageEditable: boolean;
  messageLoaded: boolean;
  validMessage: boolean;
  
  constructor(
    private fortuneService: FortuneService,
    private messageService: MessageService) {
  }
  
  initialize() {
    this.cookieImage = '/assets/images/closed-cookie.png';
    this.changeText = 'Change';
    
    this.showMessage = false;
    this.cookieOpened = false;
    this.messageEditable = false;
    this.messageLoaded = false;
    this.validMessage = false;
  }
  
  ngOnInit() {
    this.initialize();
  }
  
  getRandomFortune(): void {
    this.fortuneService.getRandomFortune()
      .subscribe(fortune => this.selectedFortune = fortune);
    
    // this.initialize();  // TODO: optimize this, currently hacky
    
    // TODO: make sure to only check this on success
    this.messageLoaded = true;
    this.messageEditable = false;
  }
  
  updateMessage(message: string): void {
    this.saveFortune(this.selectedFortune);
  }
  
  saveFortune(fortune: Fortune): void {
    this.fortuneService.updateFortune(fortune).subscribe();
  }
  
  onCookieClick(): void {
    if (this.cookieOpened) {
      this.initialize();
    } else {
      this.cookieOpened = true;
      this.cookieImage = '/assets/images/opened-cookie.png';
      
      this.showMessage = true;
      this.getRandomFortune();
    }
  }
  
  onChangeClick(): void {
    if (this.messageEditable) {
      this.changeText = 'Change';
      this.messageEditable = false;
    } else {
      this.changeText = 'Cancel';
      this.messageEditable = true;
    }
  }
  
  onSaveClick(): void {
    this.updateMessage(this.selectedFortune.message);
    alert('Updated fortune!');
    this.initialize();
  }
  
  isMessageEditable(): boolean {
    return this.messageEditable;
  }
  
  isMessageLoaded(): boolean {
    return this.messageLoaded;
  }
  
  isMessageSavable(): boolean {
    if (!this.messageEditable) { return false; }
  
    let message = this.selectedFortune.message.trim();
    if (!message) {
      this.validMessage = false;
    } else {
      this.validMessage = true;
    }
    
    return this.validMessage;
  }
  
  private log(message: string) {
    this.messageService.add('Cookies: ' + message);
  }
}
