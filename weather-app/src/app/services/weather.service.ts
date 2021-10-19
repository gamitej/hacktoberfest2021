import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class WeatherService {
  private readonly apiKey: string = '<YOUR API KEY>';

  constructor(private _http: HttpClient) {}

  getWeather(city: string, country: string) {
    const apiUrl = `https://api.openweathermap.org/data/2.5/forecast?q=${city},${country}&appid=${this.apiKey}`;
    return this._http.get(apiUrl);
  }
}
