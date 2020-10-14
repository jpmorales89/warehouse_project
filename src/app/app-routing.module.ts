import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AddProductComponent } from './components/add-product/add-product.component';
import { ListProductComponent } from './components/list-product/list-product.component';


const routes: Routes = [
  { path:'',redirectTo: 'index', pathMatch: 'full'},
  { path:'api/products',component: AddProductComponent},
  { path:'api/product-list',component: ListProductComponent},
  { path:'api/edit-product',component: AddProductComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
