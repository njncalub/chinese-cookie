import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { CookiesComponent } from './cookies/cookies.component';
import { MessagesComponent } from './messages/messages.component';

import { FortuneService } from 'app/services/fortune.service';
import { MessageService } from 'app/services/message.service';


@NgModule({
  declarations: [
    AppComponent,
    CookiesComponent,
    MessagesComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [ FortuneService, MessageService ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
