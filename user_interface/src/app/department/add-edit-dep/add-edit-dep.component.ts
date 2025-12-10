import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-add-edit-dep',
  templateUrl: './add-edit-dep.component.html',
  styleUrls: ['./add-edit-dep.component.css']
})
export class AddEditDepComponent {

  constructor() {}

  @Input() dep:any;
  DepartmentID:string;
  DepartmentName:string;

  ngOnInit():void {
    this.DepartmentID=this.dep.DepartmentID;
    this.DepartmentName=this.DepartmentName;
  }

  addDepartment() {
    var val = {DepartmentID:this.DepartmentID, DepartmentName:this.DepartmentName};
    this.service.addDepartment(val).subscribe(res=>{
      alert(res.toString());
    });
  }

  updateDepartment() {
    var val = {DepartmentID:this.DepartmentID, DepartmentName:this.DepartmentName};
    this.service.updateDepartment(val).subscribe(res=>{
      alert(res.toString());
    });

  }

}
