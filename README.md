# oci_workshop_scripts

_Oracle Workshop Extension_ used in the OCI Console to help guide on using common OCI resources and use cases. 

[Install on Chrome Browser Here](https://chrome.google.com/webstore/detail/oci-workshop-extension/pjonegmmmclaihfglajojmfcpfambpcd)

![Screenshot](/OCIExtension.jpg)

Scripts are in JSON format and have a standard outline.

JSON Outline Example: 
```\

{
  "name":"Tutorial Title",
  "description": "Description of tutorial.", 
  "steps": [
    {
      "message": "Step 1: Content of the tutorials goes here. Path specifies which location page the user should be in within OCI. Such as / would be homepage.",
      "path": "/"
    },
    {
      "message": "Step 2.",
      "path": "/block-storage/volumes"
    }
  ]
}
```

Content Outline: 
> **Overview Section**: Description of the feature or use-case.   
> **Steps**: Step by step instructions on how to complete each step.  
> * *Tips*: Tips are represented in ```<small><em>Tip:</em> Extra fact.</small>```  
>   * Shown as <small>*Tip:* Extra fact.</small>   
>* *Images*: Images should be used to help guide users through steps.Images *MUST* be in 72 dpi.
>   * They're shown as `{{img-url:/images/tutorials/iduser.png}}` in the code. 
>* Html `<h1>, <h2>, <h3>, <h4>, <a>, <strong>, <em>, and <br>` tags can be used normally to format the pages.  
>* Use h4 tags for titles on each page such as `<h4>3.1 Create Load Balancer</h4>`  
>* Use **Bold** to emphasize OCI keyworks and menu items to click. Such as `<strong>\"Load Balancers\"</strong>`  
>
>**Conclusion:** Summarize what was accomplished and feel free to provide extra documentation.    
>* If you want to link to a different module of the extension use .next-step class in a tag like this: `<a class='next-step' href='/subnets.json'>1.4 Create Subnets</a>`


<hr>

Tutorials:
* Identity and Access Management
   * Create Compartments
   * Create a User, and Groups
   * User Credentials
   * Grant Policies to Groups
   * Federation
* Governance
   * Manage Tags
   * Audit*
* Networking
   * Create VCN
   * Create Security Lists 
   * Create Route Table
   * Create Subnet
   * Create Internet Gateway
   * Reserve Public IP
* Compute
  * Create Compute
  * Create Oracle Marketplace images*
  * Create Custom Compute*
* Block Storage 
   * Create and Attach
   * Clone and Backup*
* Object Storage 
   * Create, Upload, and Download
   * Create Pre-Authenticated Requests*
* File Storage*
   * Create File Storage
* Databases*
* Advanced Networking*
   * NAT Gateway 
   * Service Gateway 
   * Local VCN peering
   * Regional VCN Peering
* Advanced Topics
   * Jump Server Load Balancer

 *Soon to be created topics.
   
    



    
