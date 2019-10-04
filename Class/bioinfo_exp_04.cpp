#include<iostream>
using namespace std;

bool bool_judge(double a , double b)
{
 if (a == b)
  return true;
 else
  return false;
}

class Matrix
{
private:

public:
 double a,b,c,d;
 Matrix(){}
 Matrix(double x, double y, double z , double w)
 {
  a = x; b = y;
  c = z; d = w;
 }
 Matrix operator + (const Matrix &q) const
 {
   Matrix m;
   m.a = a + q.a;
   m.b = b + q.b;
   m.c = c + q.c;
   m.d = d + q.d;
   m.matrix_print(); 
   return m;
 }
 
 Matrix operator * (const Matrix &q) const
 {
  Matrix m;
  m.a = a * q.a + b * q.c;
  m.b = a * q.b + b * q.d;
  m.c = c * q.a + d * q.c;
  m.d = c * q.b + d * q.d;
  m.matrix_print();
  return(m);
 }
 void matrix_print();  
 void trace(); 
 void inverse();
 Matrix operator == (const Matrix &q) const
 {
  Matrix m;
  m.a = bool_judge(a,q.a);
  m.b = bool_judge(b,q.b);
  m.c = bool_judge(c,q.c);
  m.d = bool_judge(d,q.d);
  
  if (m.a*m.b*m.c*m.d == 1)//全てTrueなら積は１になる
   return(q);
  else if (m.a*m.b*m.c*m.d== 0)//一つでも違う要素があれば積は０になる
   return(m); 
  else 
   cout << "error." << endl;
   return (m);
 }
};

void Matrix::matrix_print()
{
 cout << a <<" " << b << endl;
 cout << c <<" " << d << endl;
}
void Matrix::trace() 
{
 double trM;
 trM = a + d;
 cout << trM << endl;
 
}
void Matrix::inverse() 
{
 Matrix m;
 double det=a*d-b*c;
 m.a = d / det;
 m.b = - b / det ;
 m.c = -c / det ;
 m.d = a / det;
 m.matrix_print();
 
}


int main(void)
{
 Matrix p(3.23, 1.24, 5.13, 1.34);
 Matrix q(2.22, 4.21, 3.75, 2.18);
 cout << "P" << endl;
 p.matrix_print();
 cout << "Q" << endl;
 q.matrix_print();
 cout << "P+Q" << endl;
 Matrix r = p + q;
 cout << "P*Q" << endl;
 Matrix s = p * q;
 cout << "trace P" << endl;
 p.trace();
 cout << "trace Q" << endl;
 q.trace();
 cout << "P inverse" << endl;
 p.inverse();
 cout << "Q inverse" << endl;
 q.inverse();
 Matrix compare =  p == q;
 cout << "P == Q (if false, zero-matrix is displayed. )" << endl;
 compare.matrix_print();


 return 0;
}

