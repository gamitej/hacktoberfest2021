import { Component, OnInit } from '@angular/core';
import { WeatherService } from 'src/app/services/weather.service';

@Component({
  selector: 'app-weather',
  templateUrl: './weather.component.html',
  styleUrls: ['./weather.component.css'],
})
export class WeatherComponent implements OnInit {
  city: any = '';
  country: any = '';
  weather: any = null;

  constructor(private _weatherService: WeatherService) {}

  ngOnInit(): void {}

  getDate(str: string) {
    return str.split(' ')[0];
  }

  getTime(str: string) {
    return str.split(' ')[1];
  }

  displayWeather() {
    this._weatherService.getWeather(this.city, this.country).subscribe(
      (data) => (this.weather = data),
      (err) => console.log(err)
    );
  }
}
