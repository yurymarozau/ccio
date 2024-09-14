import { HttpClient } from '@angular/common/http';
import { Component, Injectable } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Observable } from 'rxjs';


@Injectable({
    providedIn: 'root',
})
class TestService {
    constructor(private http: HttpClient) {
    }

    public test(): Observable<any> {
        return this.http.get<any>('/api/');
    }
}

@Component({
    selector: 'app-root',
    standalone: true,
    imports: [RouterOutlet],
    templateUrl: './app.component.html',
    styleUrl: './app.component.css'
})
export class AppComponent {
    title = 'ccio';

    constructor(private test_service: TestService) {
    }

    public ngOnInit(): void {
        this.test_service.test().subscribe({
            next: (v) => console.log(v),
            error: (e) => console.log(e),
            complete: () => console.log('complete')
        })
    }
}
