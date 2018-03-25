import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable } from 'rxjs/Observable';
import { of } from 'rxjs/observable/of';
import { catchError, map, tap } from 'rxjs/operators';

import { Fortune } from 'app/models/fortune';

import { MessageService } from 'app/services/message.service';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class FortuneService {
  
  private baseApiUrl = 'http://localhost:8080/fortunes';
  
  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }
  
  /** GET: all fortunes from the server */
  getFortunes (): Observable<Fortune[]> {
    const url = `${this.baseApiUrl}/all`;
    return this.http.get<Fortune[]>(url)
      .pipe(
        tap(heroes => this.log(`fetched fortunes`)),
        catchError(this.handleError('getFortunes', []))
      );
  }
  
  /** GET: fortune by UUID. Return `undefined` when UUID not found */
  getFortuneNo404<Data>(uuid: string): Observable<Fortune> {
    const url = `${this.baseApiUrl}/${uuid}/`;
    return this.http.get<Fortune[]>(url)
      .pipe(
        map(fortunes => fortunes[0]),
        tap(f => {
          const outcome = f ? `fetched` : `did not find`;
          this.log(`${outcome} fortune uuid=${uuid}`);
        }),
        catchError(this.handleError<Fortune>(`getFortune uuid=${uuid}`))
      );
  }
  
  /** GET: fortune by UUID. Will 404 if UUID not found */
  getFortune(uuid: string): Observable<Fortune> {
    const url = `${this.baseApiUrl}/${uuid}/`;
    return this.http.get<Fortune>(url).pipe(
      tap(f => this.log(`fetched fortune ${f.uuid}`)),
      catchError(this.handleError<Fortune>(`getFortune uuid=${uuid}`))
    );
  }
  
  /** GET: random fortune.  */
  getRandomFortune(): Observable<Fortune> {
    const url = `${this.baseApiUrl}/`;
    return this.http.get<Fortune>(url).pipe(
      tap(fortune => this.log(`fetched random fortune ${fortune.uuid}`)),
      catchError(this.handleError<Fortune>(`getFortune <random>`))
    );
  }
  
  /** PUT: update the fortune on the server */
  updateFortune (fortune: Fortune): Observable<any> {
    const url = `${this.baseApiUrl}/${fortune.uuid}/?message=${fortune.message}`;
    return this.http.patch(url, fortune, httpOptions).pipe(
      tap(_ => this.log(`updated fortune uuid=${fortune.uuid}`)),
      catchError(this.handleError<any>('updateFortune'))
    );
  }
  
  /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead
      
      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);
      
      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }
  
  /** Log a FortuneService message */
  private log(message: string) {
    this.messageService.add('FortuneService: ' + message);
  }
}
