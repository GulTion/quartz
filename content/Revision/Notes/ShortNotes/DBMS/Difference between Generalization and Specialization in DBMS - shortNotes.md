---
subject: DBMS
type: ShortNotes
sr-due: 2023-12-18
sr-interval: 2
sr-ease: 150
---
#note/DBMS
Generalization and specialization are the **Enhanced Entity Relationship diagram** (EER-diagram)

**1. Generalization :**  
It works on the principle of<mark style="background: #FF5582A6;"> bottom up approach</mark>. In Generalization lower level functions are combined to form higher level function which is called as entities. This process is repeated further to make advanced level entities.

In the Generalization process properties are drawn from particular entities and thus we can create generalized entity. We can summarize Generalization process as it combines subclasses to form superclass.

**Example of Generalization –**  
Consider two entities Student and Patient. These two entities will have some characteristics of their own. For example Student entity will have Roll_No, Name and Mob_No while patient will have PId, Name and Mob_No characteristics. Now in this example Name and Mob_No of both Student and Patient can be combined as a Person to form one higher level entity and this process is called as Generalization Process.

![](https://media.geeksforgeeks.org/wp-content/uploads/20200422233403/Generalisation_1.jpg)

**2. Specialization :**  
We can say that Specialization is opposite of Generalization. In Specialization things are broken down into smaller things to simplify it further. We can also say that in Specialization a particular entity gets divided into sub entities and it’s done on the basis of it’s characteristics. Also in Specialization Inheritance takes place.

**Example of Specialization –**  
Consider an entity Account. This will have some attributes consider them Acc_No and Balance. Account entity may have some other attributes like Current_Acc and Savings_Acc. Now Current_Acc may have Acc_No, Balance and Transactions while Savings_Acc may have Acc_No, Balance and Interest_Rate henceforth we can say that specialized entities inherits characteristics of higher level entity.

![](https://media.geeksforgeeks.org/wp-content/uploads/20200422233542/Specialisation_1.jpg)

After applying generalization and specialization, the structure of resultant figures are same.

  
  
**Difference between Generalization and Specialization :**

|GENERALIZATION|SPECIALIZATION|
|---|---|
|Generalization works in Bottom-Up approach.|Specialization works in top-down approach.|
|In Generalization, size of schema gets reduced.|In Specialization, size of schema gets increased.|
|Generalization is normally applied to group of entities.|We can apply Specialization to a single entity.|
|Generalization can be defined as a process of creating groupings from various entity sets|Specialization can be defined as process of creating subgrouping within an entity set|
|In Generalization process, what actually happens is that it takes the union of two or more lower-level entity sets to produce a higher-level entity sets.|Specialization is reverse of Generalization. Specialization is a process of taking a subset of a higher level entity set to form a lower-level entity set.|
|Generalization process starts with the number of entity sets and it creates high-level entity with the help of some common features.|Specialization process starts from a single entity set and it creates a different entity set by using some different features.|
|In Generalization, the difference and similarities between lower entities are ignored to form a higher entity.|In Specialization, a higher entity is split to form lower entities.|
|There is no inheritance in Generalization.|There is inheritance in Specialization.|
