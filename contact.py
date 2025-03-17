class Contact:
      def __init__(self,first_name,last_name,address,city,state,zip_code,phone_number,email_id):
            self.first_name=first_name
            self.last_name=last_name
            self.address=address
            self.city=city
            self.state=state
            self.zip_code=zip_code
            self.phone_number=phone_number
            self.email_id=email_id
      def __str__(self):
            return (f"Name: {self.first_name} {self.last_name}\n Address: {self.address}, {self.city}, {self.state} - {self.zip_code}\n Phone: {self.phone_number}\n Email: {self.email_id}")